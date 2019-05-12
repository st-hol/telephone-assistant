def parse_result_set(rows):
    """
    Parses result after fetching.
           :param rows of fetched
           :return list
    """
    rows = [item[1] for item in rows]
    return rows
