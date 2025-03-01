try:
  usia_input = input("Masukan usia anda: ")

  try:
    usia = int(usia_input)
  except valueEror:
    usia = usia_input(usia_input.lower())

  if usia < 18:
    print("Anda masih anak-anak.")
  elif usia < 60:
    print("Anda adalah orang dewasa.")
  else:
    print("Anda sudah lansia.")
