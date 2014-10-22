matlib-plotter
==============

A simple python matlib plotting interface

####Overview:
	This plotting class uses the matplotlib library and has the capability of reading in CSV files, plotting a graph of the data within the file, and exporting the plots as a PNG.  It is designed to have one master function that, provided the file name, desired fields, and time period, will produce the graph of the data.  The following path can be used to locate the file in our control-tower repository on Git Hub: control-tower/ control-sync/ plotting, and is titled *Plot_Class.py*.  This class is compatible with Python 2.7 and 3.4.


####How The Class Works:
	The Python Plotting Class contains all the member variables and functions necessary to plot a graph from a CSV file.  The *__init__()* function, which is required for classes, is used to initialize the object and set all the member variables.  Following the initialization of the class are all the functions needed to plot data.
	Basic functions are contained in this class.  To begin organizing the data, the *convert_to_float()* function converts strings into the float (allows decimals) data type.  A *get_data()* function extracts the data from any specified field other than time.  The *convert_date()* function focuses primarily on converting date and time information in strings into the DateTime type, which is readable by other Python libraries.  Converting the date and time is necessary to create a proper x-axis for the plot to display the time period.
	Function *gather_dates()* uses the beginning and ending index to return the range of the dates, and *gather_chosen()* uses the beginning and ending index to return the chosen data in the time range.  The *gather_chosen()* function uses the DateTime conversion and the desired field input to locate the data of a certain field within a certain period.  The find_index() function is used to find the indices of a time range in order to find the corresponding data within it.  This requires the use of an iterator to locate the indices for the field within the period.
	A function was also created to format the legend.  The *set_field_names()* function sets the titles of the fields as they will appear on the legend of the graph.  If the user has already entered names for the fields, these are used.  Alternatively, if no field names have been entered, the field name in the header of the CSV file is changed to a more specific, unabbreviated name with units.
	A few functions in this class utilize these basic functions.  The *input_time()* function uses the *convert_date()* function to convert the date strings to DateTime objects followed by the *find_index()* function to find the indices of the time range when provided the beginning date and time and ending date and time for the range.  Within the *input_time()* function, the *gather_dates()* function is then used to obtain the x-axis values for the plot.  An *input_field()* function was also written which when provided the fields the user wishes to plot, uses the *get_data()* function to gather the data from the specified field and then the *gather_chosen()* function to get the y-axis values for the plot.  Lastly, the *plot_data()* function plots the data on a graph using a scatter plot, creates a legend for the graph, and saves the graph as a PNG.  The original specifications of the plotting class were to export the graph as a JPEG.  matplotlib does not support exporting graphs as JPEGs, so the code was edited to export the plots as PNG files using the *savefig()* function in matplotlib.

Data Used:
	Currently the data from the *215_data.csv* file is being used which can also be found in the same directory of the *Plot_Class.py* file.  This is the data from the box located at Hokulani Elementary School from May 26 at 12:00 am HST to May 29 at 9:56:14 pm.  This box measures current uptime in milliseconds, temperature in decacelcius, pressure in pascals, battery voltage in millivolts, panel voltage in millivolts, solar irradiance sensor voltage in millivolts, solar irradiance in W/m2, humidity in hectopercent, and the number of times the current uptime timer has overflowed.


####To Use:
	In the plotting class titled Plot_Class.py, the user can plot graphs from a csv file.  To do this the user should first set the properties of the graph by using a dictionary.  The dictionary needs to have:
•	A title for the graph (title)
•	Title for the x-axis of the graph (x_axis)
•	Title for the y-axis of the graph (y_axis)
•	Titles for the fields for the legend in a list in the order of the fields in the CSV file (field_titles)
•	Colors to be used for the different fields in a list (colors)
The names of the keys in the dictionary for the described properties above need to be set to the words in the parentheses.  If the user would not like to specify certain fields, they can just input an empty string or list.  If a title is not input by the user, a title will not appear for the graph or axis.  If a list of names for the fields for the legend is not input by the user, a list of more specific names including the units for the field will be used instead.  If the user does not input a list of colors, a set of random colors is used.  An example of a dictionary specifying the properties of the graph can be found below.

plot_prop = {'title':'Weather Box Data', 'x_title':'Time', 'y_title': '', 'field_titles':[],'colors':[]}

	Following this, the user will create an instance of the plotting class.  In creating this instance, the user will input:
•	Name of the CSV file
•	Start date and time for the data the user wishes to plot
•	End date and time for the data the user wishes to plot
•	Fields the user wishes to plot in a list
•	Dictionary for the plotting properties
•	True or False for whether or not the user would like to plot all the fields in the CSV file
The name of the CSV file needs to be entered exactly as the file is titled.  The start and end date and time need to be entered in the following format: YYYY-mm-dd HH:MM:SS.ffffff-zz, where Y is the year, m is the month, d is the day, H is the hour, M is the minutes, S is the seconds, f is the microseconds, and z is the UTC offset.  The CSV file needs to be in the same directory as the Python plotting class.  Even if a list of fields is entered by the user, if True is set for whether or not the user would like to plot all fields of the CSV file, all fields will be plotted.  An example of creating an instance of the plotting class is provided below.

weatherbox = Plotting('215_data.csv', '2014-05-26 00:00:00.000000-10', '2014-05-29 21:56:14.000000-10', ['apogee_w_m2','panel_mv','batt_mv','bmp085_temp_decic'], plot_prop, True)

	To plot the data in a graph, the user can call the plot_data() function which plots the data as a scatter plot and saves the graph as a PNG file.  It save the file to the directory the Python plotting class is in.

weatherbox.plot_data()

	After all data has been plotted from a specific data file, the file the data is being retrieved from should be closed with the command below.

weatherbox.openfile.close()


####Results:
	After running the commands above, a graph of the data fields selected over the specified time range will be plotted as a scatter graph.  The legend for the graph appears centered at the top of the graph in four columns.  This graph is saved as a PNG file to the directory the Python plotting class is currently located in.
	Currently following the example above, this code prints the following graph in Figure 1.  This is the data from the 215_data.csv file, and the time interval specified spans all four days of data contained in it.  In Figure 1, the four days can clearly be seen on the x-axis, and there are four peaks on the graph.  Although a list of field names to plot was entered, the user indicated that they would like to plot all fields in the file, so all thirteen fields are graphed below.  The title of the graph and the x-axis are labeled as specified in the plotting properties dictionary above.  Since the field names and color scheme are not specified, they are retitled to more specific names for the data they are plotting, and the colors for each field are randomly picked.
