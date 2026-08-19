def first_derivative(value, fun, step_size):
    """Implement the finite difference approach to estimate the first derivative.

    Keyword arguments:
    value      -- (float) the starting value to estimate first derivative
    fun        -- (function) the function that we will be differentiating
    step_size  -- (float) the epsilon

    Returns: a float of the first derivative estimate
    """
    return (fun(value + step_size) - fun(value)) / step_size

def second_derivative(value, fun, step_size):
    """Implement the finite difference approach to estimate the second derivative.

    Keyword arguments:
    value      -- (float) the starting value to estimate first derivative
    fun        -- (function) the function that we will be differentiating
    step_size  -- (float) the epsilon

    Returns: a float of the second derivative estimate
    """
    # implement finite difference approach to estimate derivative 
    return (fun(value + 2 * step_size) - (2 * fun(value + step_size)) + fun(value)) / (step_size**2)

def optimize(start, fun, stop_criteria = 0.1, step_size = 0.1):
    """Implement a function for optimizing or finding the point at which the function 
    reaches a minimum/maximum point.

    Keyword arguments:
    start          -- (float) the starting value to begin Newton's method
    fun            -- (function) the function that we will be differentiating
    stop_criteria  -- (float) the epsilon
    step_size      -- (float) the stopping condition

    Returns: a float of the second derivative estimate
    """
    # calculate next_value using start 
    first_der = first_derivative(start, fun, step_size)
    second_der = second_derivative(start, fun, step_size)
    next_value = start - (first_der / second_der)
    
    # base case (stop recursion)
    if (abs(next_value - start) <= stop_criteria):
        return next_value

    # recursive case
    return optimize(next_value, fun, stop_criteria, step_size)

