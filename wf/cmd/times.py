def single(cmd, args, funs, vars, consts, exec_stack, exec, pval):
  # if true (=1) returned, it stops the loop

  if len(args) != 2:
    print("Invalid arguments for \"times\" command!")
    return False

  fname = args[1]
  var = args[0]

  if not fname in funs.keys():
    print("Function given to \"times\" command is not defined!")
    return False

  fun = funs[fname]

  if fun[0] > 0:
    print("Function given to \"times\" command cannot have arguments!")
    return False

  ftype = fun[1]

  if not var in vars.keys():
    print("Variable given to \"times\" command is not defined!")
    return False

  am = vars[var]

  del vars[var]

  consts[var] = 0

  oldr = vars["R"] if "R" in vars.keys() else False

  for i in range(int(am)):
    if not var in consts.keys():
      print("Variable given to \"times\" suddenly dissapeared!")
      return False

    consts[var] = i

    if ftype == "!":
      stack = exec_stack(fun[2], [], pval, exec, funs, vars, consts)
      if len(stack) > 0 and stack[-1] == 1:
        break

    elif ftype == "%":
      vars["R"] = 0.0
      exec(0, fun[2])
      if vars["R"] == 1:
        if oldr == False:
          del vars["R"]
        break
      if oldr == False:
        del vars["R"]

    else:
      print("Type of function \"" + name + "\" is not implemented!")

      del consts[var]
      vars[var] = am

      return False

  del consts[var]
  vars[var] = am

  return True