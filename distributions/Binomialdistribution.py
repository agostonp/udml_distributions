from .Generaldistribution import Distribution
import math
import matplotlib.pyplot as plt


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    #   A binomial distribution is defined by two variables:
    #       the probability of getting a positive outcome
    #       the number of trials

    #   If you know these two values, you can calculate the mean
    #   and the standard deviation

    #   For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #   You can then calculate the mean and standard deviation
    #   with the following formula:
    #       mean = p * n
    #       standard deviation = sqrt(n * p * (1 - p))

    def __init__(self, p, n):
        self.p = float(p)
        self.n = int(n)

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean = self.p * self.n
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev = math.sqrt(self.n * self.p * (1.0 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set.
           The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        # sum(self.data) equals the count of positive trials
        self.p = sum(self.data) / self.n
        self.calculate_mean()
        self.calculate_stdev()
        return self.p, self.n

    def plot_bar(self):
        """Function to output a bar chart of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.bar(range(self.n), self.data)
        plt.title('Bar chart of Data')
        plt.xlabel('trials')
        plt.ylabel('result')
        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        comb = (math.factorial(self.n) /
                (math.factorial(self.n-k) * math.factorial(k)))
        return comb * self.p**k * (1.0-self.p)**(self.n-k)

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        x_values = list(range(self.n+1))
        y_values = [self.pdf(x) for x in x_values]
        plt.bar(x_values, y_values)
        plt.title('Probability Density Function')
        plt.xlabel('k')
        plt.ylabel('Density')
        plt.show()

        return x_values, y_values

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            print(error)
            raise

        return Binomial(self.p, self.n + other.n)

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """

        return "mean {}, standard deviation {}, p {}, n {}".format(
                self.mean, self.stdev, self.p, self.n)
