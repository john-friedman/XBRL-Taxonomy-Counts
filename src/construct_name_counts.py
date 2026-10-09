from datamulehub import databases


# $1.03 as of 10/9/2026
databases.query(
    "SELECT name, COUNT(*) AS count FROM simple_xbrl GROUP BY name ORDER BY count DESC",
    output_dir="simple_xbrl_taxonomy_counts",
)