temps = [35, 41, 37 ,39 ,52]

new_temps = [ temp / 10 for temp in temps]
# In line for loops for lists

temps = [35, 41, 37 ,39 ,52 ,-9999]

new_temps = [ temp / 10 for temp in temps if temp != -9999]
# In line loops with conditional

temps = [35, 41, 37 ,39 ,52]

new_temps = [ temp / 10 if temp != -9999 else 0 for temp in temps]
# When using a if/else conditional, conditional comes before the for/in statement

