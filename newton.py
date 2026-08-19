def optimize(start, fun, stop_criteria = 0.1, step_size = 0.1):

    # calculate next_value using start 
    first_der = first_derivative(start, fun, step_size)
    second_der = second_derivative(start, fun, step_size)
    next_value = start - (first_der / second_der)
    
    # base case (stop recursion)
    if (abs(next_value - start) <= stop_criteria):
        return next_value

    # recursive case
    return optimize(next_value, fun, stop_criteria, step_size)


def first_derivative(value, fun, step_size):
    # implement finite difference approach to estimate derivative 
    return (fun(value + step_size) - fun(value)) / step_size

def second_derivative(value, fun, step_size):
    # implement finite difference approach to estimate derivative 
    return (fun(value + 2 * step_size) - (2 * fun(value + step_size)) + fun(value)) / (step_size**2)
