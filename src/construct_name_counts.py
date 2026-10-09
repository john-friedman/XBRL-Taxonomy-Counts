from datamulehub import databases

databases.query(
    "SELECT name, COUNT(*) AS count FROM simple_xbrl GROUP BY name ORDER BY count DESC",
    output_dir="simple_xbrl_taxonomy_counts",
)