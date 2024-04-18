#%% https://github.com/moshi4/pyCirclize

from pycirclize import Circos
import pandas as pd

# Create matrix data (10 x 10)
row_names = list("ABCDEFGHIJ")
col_names = row_names
matrix_data = [
    [51, 115, 60, 17, 120, 126, 115, 179, 127, 114],
    [108, 138, 165, 170, 85, 221, 75, 107, 203, 79],
    [108, 54, 72, 123, 84, 117, 106, 114, 50, 27],
    [62, 134, 28, 185, 199, 179, 74, 94, 116, 108],
    [211, 114, 49, 55, 202, 97, 10, 52, 99, 111],
    [87, 6, 101, 117, 124, 171, 110, 14, 175, 164],
    [167, 99, 109, 143, 98, 42, 95, 163, 134, 78],
    [88, 83, 136, 71, 122, 20, 38, 264, 225, 115],
    [145, 82, 87, 123, 121, 55, 80, 32, 50, 12],
    [122, 109, 84, 94, 133, 75, 71, 115, 60, 210],
]
matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# Initialize from matrix (Can also directly load tsv matrix file)
circos = Circos.initialize_from_matrix(
    matrix_df,
    space=3,
    r_lim=(93, 100),
    cmap="tab10",
    ticks_interval=500,
    label_kws=dict(r=94, size=12, color="white"),
)

print(matrix_df)
fig = circos.plotfig()

#%% https://github.com/moshi4/pyCirclize

from pycirclize import Circos
from pycirclize.utils import ColorCycler

# Provide paths to your local files
chr_bed_file = '/Users/fvashegh/Library/CloudStorage/OneDrive-JNJ/RESOLVE/circlize/hg38_chr.bed'
cytoband_file = '/Users/fvashegh/Library/CloudStorage/OneDrive-JNJ/RESOLVE/circlize/hg38_cytoband.tsv'
chr_links_file = '/Users/fvashegh/Library/CloudStorage/OneDrive-JNJ/RESOLVE/circlize/hg38_genomic_link.tsv'

class ChrLink:
    def __init__(self, query_chr, query_start, query_end, ref_chr, ref_start, ref_end):
        self.query_chr = query_chr
        self.query_start = query_start
        self.query_end = query_end
        self.ref_chr = ref_chr
        self.ref_start = ref_start
        self.ref_end = ref_end

# Read chr_links data from the file and convert to ChrLink objects
chr_links = []
with open(chr_links_file, 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        chr_links.append(ChrLink(
            query_chr=parts[0],
            query_start=int(parts[1]),
            query_end=int(parts[2]),
            ref_chr=parts[3],
            ref_start=int(parts[4]),
            ref_end=int(parts[5])
        ))

# Initialize Circos from BED chromosomes
circos = Circos.initialize_from_bed(chr_bed_file, space=3)
circos.text("Homo sapiens\n(hg38)", deg=315, r=150, size=12)

# Add cytoband tracks from cytoband file
circos.add_cytoband_tracks((95, 100), cytoband_file)

# Create chromosome color dict
ColorCycler.set_cmap("hsv")
chr_names = [s.name for s in circos.sectors]
colors = ColorCycler.get_color_list(len(chr_names))
chr_name2color = {name: color for name, color in zip(chr_names, colors)}

# Plot chromosome name & xticks
for sector in circos.sectors:
    sector.text(sector.name, r=120, size=10, color=chr_name2color[sector.name])
    sector.get_track("cytoband").xticks_by_interval(
        40000000,
        label_size=8,
        label_orientation="vertical",
        label_formatter=lambda v: f"{v / 1000000:.0f} Mb",
    )

# Plot chromosome link
for link in chr_links:
    region1 = (link.query_chr, link.query_start, link.query_end)
    region2 = (link.ref_chr, link.ref_start, link.ref_end)
    color = chr_name2color[link.query_chr]
    if link.query_chr in ("chr1", "chr8", "chr16") and link.query_chr != link.ref_chr:
        circos.link(region1, region2, color=color)

fig = circos.plotfig()