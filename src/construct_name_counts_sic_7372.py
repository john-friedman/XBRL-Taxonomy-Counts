from datamulehub import databases

# $0.1048 as of 10/9/2026
databases.query(
    """
    SELECT x.name, COUNT(*) AS count
    FROM simple_xbrl x
    WHERE EXISTS (
        SELECT 1
        FROM sec_accession_cik_table c
        JOIN filer_metadata f ON f.cik = c.cik
        WHERE c.accessionnumber = x.accessionnumber
          AND f.sic = '7372'
    )
    GROUP BY x.name
    ORDER BY count DESC
    """,
    output_dir="simple_xbrl_name_counts_sic_7372",
)