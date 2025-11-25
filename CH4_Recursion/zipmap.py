def zipmap(keys, values):
 
  if len(keys) == 0 or len(values) == 0:
    return {}

  smaller = zipmap(keys[1:], values[1:])
  smaller[keys[0]] = values[0]

  return smaller