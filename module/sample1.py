# #import method
# import sample
# sample.demo()
# print(sample.data)

#import in content
# #used in rename method
# import sample as s
# s.demo()
# print(s.data)

from sample import demo,data
demo()
print(data)


from sample import * #* mentioned in all functions
demo()
print(data)


