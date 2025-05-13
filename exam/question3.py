def remove_duplicates_ordered(data):
  """Removes duplicates from a list while preserving order."""
  seen = set()
  result = []
  for item in data:
    if item not in seen:
      result.append(item)
      seen.add(item)
  return result
