def sum_nested_list(lst):
  res = 0
  for el in lst:
    if isinstance(el, int):
      res += el
    if isinstance(el, list):
      res += sum_nested_list(el)
  
  return res