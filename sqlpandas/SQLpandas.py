import re
import sys
import pandas as pd


class SQLpandas():
	
	def __init__(self,*arg,**kwarg):
		try:
			self.dataframe = pd.read_excel(*arg,**kwarg)
			return None
		except Exception as msg:
			print msg

			
	def exec_sql(self,query):
		try:	
			query = query.strip()
			tmp_query = query.lower()
			tmp_query = tmp_query.split()

			columns_list = []
			
			name_flag = 1
			value_flag = 0
			
			sql_cond_col_name = ""
			condition_string = ""
			name_flag_started = 0
			name_flag_key1_cnt = 0
			name_flag_key2_cnt = 0
			
			if tmp_query[0] == "select":
				
				if "from" in tmp_query:
					if "where" in tmp_query:
						pattern = '(?i)select (.+) (?i)from (.+) (?i)where (.+)'
					else:
						pattern = '(?i)select (.+) (?i)from (.+)'
						
					parameters = re.findall(pattern,query)
					if parameters:
						parameters = list(parameters[0])
					else:
						print "Invalid Query"
						return
 
					# Columns Processing
					if str(parameters[0]) == "*":
						sql_column_name = str(parameters[0])
					else:
						if str(parameters[0]).find(',') != -1:
							tmp_columns_list = str(parameters[0]).split(',')
							for idx,column in enumerate(tmp_columns_list):
								column = column.strip()
								columns_list.append(column)
							sql_column_name = columns_list
						else:
							sql_column_name = str(parameters[0])

					# Table name processing
					
					sql_table_name_table = str(parameters[1])
						
					# Condition Processing
					if len(parameters) > 2:
						if str(parameters[2]).count('=') == 1:
							_condition	= str(parameters[2]).split("=")
							sql_cond_col_name 	= _condition[0].strip()
							sql_cond_col_value 	= _condition[1].strip()
							if sql_cond_col_value.find("'") != -1:
								sql_cond_col_value = sql_cond_col_value.replace("'","")
						else:
							if str(parameters[2]).count('=') == 0:
								print "Invalid Condition"
							else:
								print "Only one condition is allowed"
							return

					# SELECT Query Execution
					table = pd.DataFrame(self.dataframe)
					if sql_column_name == "*":
						
						if sql_cond_col_name == "":
							result = self.dataframe
						else:
							result = table.loc[self.dataframe[sql_cond_col_name] == sql_cond_col_value]
					else:
						if sql_cond_col_name == "":
							result = self.dataframe[sql_column_name].values
						else:
							if len(columns_list) > 1:
								tmp_result = table.loc[self.dataframe[sql_cond_col_name] == sql_cond_col_value]
								result = tmp_result[columns_list]
								
							else:
								tmp_table = table.loc[self.dataframe[sql_cond_col_name] == sql_cond_col_value]
								result = tmp_table[sql_column_name].values
					
					return result
					
				else:
					print "FROM keyword is missing"
					return

			else:
				print "Only SELECT Query is allowed"
				return
				
			
			
		except:
			excp_type = str(sys.exc_info()[0])[str(sys.exc_info()[0]).find("'")+1:str(sys.exc_info()[0]).rfind("'")]
			excp_detail = str(sys.exc_info()[1])
			err_msg = 'Exception Type   : '+excp_type+'\nException Detail : '+excp_detail
			print err_msg
			
		