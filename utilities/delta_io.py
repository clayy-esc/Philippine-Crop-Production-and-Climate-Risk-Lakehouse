"""Write Delta tables. This is the only code shared between notebooks."""

def write_delta_table(df, table_name: str, mode: str = 'overwrite') -> None:
    """
    Write a DataFrame to a Unity Catalog Delta table.
        mode='overwrite' -> full refresh (default)
        mode='append'    -> add rows to the existing table 
    """
    writer = df.write.format('delta').mode(mode)
    if mode == 'append':
        writer = writer.option('mergeSchema', 'true')
    else:
        writer = writer.option('overwriteSchema', 'true')
    writer.saveAsTable(table_name)
    print(f'Wrote ({mode}): {table_name}')