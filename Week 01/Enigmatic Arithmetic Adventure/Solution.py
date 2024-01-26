#The challenge lies in accurately parsing the cryptic series, understanding the bounds, and calculating the sum within the specified range. The series may be presented in a way that requires careful interpretation, adding a layer of complexity to the task.


def cryptic_series_sum(series, bounds):
    # Extracting the series terms
    series_terms = [int(term.strip()) for term in series.split('+')]
    
    # Extracting the bounds
    start_index, end_index = map(int, bounds.split())

    # Calculating the sum within the specified range
    result = sum(series_terms[start_index - 1 : end_index])

    return result

series=input()
bounds=input()
print(cryptic_series_sum(series, bounds))
