Eduardo Ribeiro Silva de Oliveira

I discovered the bug after limiting the DataFrame window using the timedelta and min/max functions.

Additionally, I chose to build the code in such a way that it adapts to the environment variables specified in config.json, simulating the manipulation of a Lambda function in the AWS Management Console.

I used object-oriented programming and SOLID principles to abstract the problem into two components: one class responsible for obtaining and formatting the DataFrame as needed, and another class that receives this formatted DataFrame and performs the calculations. This approach allowed me to build dictionaries of the type <str, class> to define which rate handler to use, as well as <str, function> for setting the attributes based on the values read from the environment variables.

I used the logging library to approximate my debugging practices for Lambdas via CloudWatch. Empirically, I found that it is much easier to identify potential errors when using log messages at the beginning and end of each method, indicating the received parameters and the value or shape of the generated DataFrame.

The python-bcb library should easily support adding the desired behavior for monthly and yearly frequencies.

The unit tests were quite succinct and ensured the uniformity of parameter typing and the integrity of the DataFrames. A potential improvement would be to use Python's unittest library to create specific tests for the calculation functions, including extreme cases.

A possible addition in a real scenario would be the implementation of the DatabaseHandler. In this case, I chose to omit this class, as it is only necessary to save two .csv files.