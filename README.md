Eduardo Ribeiro Silva de Oliveira

I discovered the bug after limiting the DataFrame window using the timedelta and min/max functions.

Also, I chose to build the code in such a way that it would be adaptive according to the environment variables passed in config.json to simulate the manipulation of a lambda in the AWS Management HUB.

I used object-oriented programming and SOLID principles to abstract the problem into two components: one class responsible for obtaining the DataFrame and formatting it as needed and another class that receives this formatted DataFrame and performs the calculations. This way, it was possible to build dictionaries of the type <str, class> to define which rate Handler to use, as well as <str, function> for setting the attributes from the values read in the environment variables.

I used the logging library to approximate what I use to debug lambdas via CloudWatch. Empirically, I found that it is much easier to identify possible errors when using log messages at the beginning and end of each method, indicating the received parameters and what the value or shape of the generated DataFrame is.

The unit tests were quite succinct and only ensured the uniformity of parameter typing, as well as the integrity of the DataFrames. A possible improvement would be to use Python's unittest library to create specific tests for the calculation functions, with extreme examples.

A possible addition in a real example would be the implementation of the DatabaseHandler. In this case, I chose to omit this class, because it is only necessary to save two .csv files.