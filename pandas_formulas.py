
class p_func():

    def add_rows(self, df, row_list=[], column_list=[], append=False):
        """
        add a list of rows by index number for a wide form dataframe
        """
        df = df.filter(items = row_list, axis=0)
        df = pd.DataFrame(df.sum()).T
        return df

    def subtract_rows(self, df, row_list=[], column_list=[], append=False):
        """
        add a list of rows by index number for a wide form dataframe
        """
        df = df.filter(items = row_list, axis=0)
        df = df.diff().tail(1)
        #df = pd.DataFrame(df.diff()).T
        return df

    def divide_rows(self, df, row_list=[], column_list=[], append=False):
        """
        divide two rows for a wide form dataframe
        """
        df2 = pd.DataFrame(df.loc[row_list[0]]/df.loc[row_list[1]]).T    
        return df2

    def multiply_rows(self, df, row_list=[], column_list=[], append=False):
        """
        multiply two rows for a wide form dataframe
        """
        df2 = pd.DataFrame(df.loc[row_list[0]]*df.loc[row_list[1]]).T    
        return df2

    def abs_rows(self, df, row_list=[], column_list=[], append=False):
        """
        multiply two rows for a wide form dataframe
        """
        df = df.filter(items = row_list, axis=0)
        df = df.abs()
        return df

#usage: 
#pf = p_func()
#pf.subtract_rows(df,[1,2])
