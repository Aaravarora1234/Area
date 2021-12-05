Lengthunitlist = ["cm","m","km"]
Areaunitlist = ["sq.cm","sq.m","sq.km"]
while True :
    try :
        Shape = str(input("Enter a Shape (Square/Rectangle/Circle) : ")).lower()
        if (Shape == "square") :
            try :
                Side = float(input("Enter the Length of the Side : "))
                try :
                    Unit = str(input("Enter the Unit of Measurement (cm/m/km) : ")).lower()
                    if (Unit not in Lengthunitlist) :
                        raise ValueError
                    Preferredunit = str(input("Enter the Unit you want the Area to be Displayed in (sq.cm/sq.m/sq.km) : ")).lower()
                    if (Preferredunit not in Areaunitlist) :
                        raise ValueError
                    Result = Side ** 2
                    Resultunit = "sq." + Unit
                    if (Preferredunit != Resultunit) :
                        if (Preferredunit == "sq.cm") :
                            if (Resultunit == "sq.m") :
                                Result = Result * 10000
                            elif (Resultunit == "sq.km") :
                                Result = Result/10000000000
                        elif (Preferredunit == "sq.m") :
                            if (Resultunit == "sq.cm") :
                                Result = Result/10000
                            elif (Resultunit == "sq.km") :
                                Result = Result * 1000000
                        elif (Preferredunit == "sq.km") :
                            if (Resultunit == "sq.m") :
                                Result = Result/1000000
                            elif (Resultunit == "sq.cm") :
                                Result = Result/10000000000
                        Resultunit = Preferredunit
                    Area = str(Result) + " " + Resultunit
                    print("The Area of the Square is " + Area + ".")
                except : 
                    print("Please Enter a Standard Unit of Measurement. (cm/m/km)")
            except :
                print("Please Enter a Numerical Value.")
        elif (Shape == "rectangle") :
            try :
                Length = float(input("Enter the Length of the Rectangle : "))
                Breadth = float(input("Enter the Breadth of the Rectangle : "))
                try :
                    Lengthunit = str(input("Enter the Unit for Length (cm/m/km) : ")).lower()
                    if (Lengthunit not in Lengthunitlist ) :
                        raise ValueError
                    Breadthunit = str(input("Enter the Unit for Breadth (cm/m/km) : ")).lower()
                    if (Breadthunit not in Lengthunitlist) :
                        raise ValueError
                    Preferredunit = str(input("Enter the Unit you want the Area to be Displayed in (sq.cm/sq.m/sq.km) : ")).lower()
                    if (Preferredunit not in Areaunitlist) :
                        raise ValueError
                    if (Lengthunit != Breadthunit) :
                        if (Lengthunit == "cm") :
                            if (Breadthunit == "m") :
                                Length = Length/100
                                Resultunit = "sq." + Breadthunit
                            elif (Breadthunit == "km") :
                                Length = Length/100000
                                Resultunit = "sq." + Breadthunit 
                        elif (Lengthunit == "m") :
                            if (Breadthunit == "cm") :
                                Length = Length * 100
                                Resultunit = "sq." + Lengthunit
                            elif (Breadthunit == "km") :
                                Length = Length/1000
                                Resultunit = "sq." + Breadthunit
                        elif (Lengthunit == "km") :
                            if (Breadthunit == "m") :
                                Length = Length * 1000
                                Resultunit = "sq." + Lengthunit
                            elif (Breadthunit == "cm") :
                                Length = Length * 100000
                                Resultunit = "sq." + Lengthunit
                    else :
                        Resultunit = "sq." + Lengthunit
                    Result = Length * Breadth
                    if (Preferredunit != Resultunit) :
                        if (Preferredunit == "sq.cm") :
                            if (Resultunit == "sq.m") :
                                Result = Result * 10000
                            elif (Resultunit == "sq.km") :
                                Result = Result/10000000000
                        elif (Preferredunit == "sq.m") :
                            if (Resultunit == "sq.cm") :
                                Result = Result/10000
                            elif (Resultunit == "sq.km") :
                                Result = Result * 1000000
                        elif (Preferredunit == "sq.km") :
                            if (Resultunit == "sq.m") :
                                Result = Result/1000000
                            elif (Resultunit == "sq.cm") :
                                Result = Result/10000000000
                        Resultunit = Preferredunit
                    Area = str(Result) + " " + Resultunit
                    print("The Area of the Rectangle is " + Area + ".")
                except :
                    print("Please Enter a Standard Unit of Measurement. (cm/m/km) or (sq.cm/sq.m/sq.km)")
            except :
                print("Please Enter a Numerical Value.")
        elif (Shape == "circle") :
            try :
                Radius = float(input("Enter the Radius of the Circle : "))
                try :
                    Unit = str(input("Enter the Unit of Measurement (cm/m/km) : ")).lower()
                    if (Unit not in Lengthunitlist):
                        raise ValueError
                    Preferredunit = str(input("Enter the Unit you want the Area to be Displayed in (sq.cm/sq.m/sq.km) : ")).lower()
                    if (Preferredunit not in Areaunitlist) :
                        raise ValueError
                    Result = (22/7) * Radius ** 2
                    Resultunit = "sq." + Unit
                    if (Preferredunit != Resultunit) :
                        if (Preferredunit == "sq.cm") :
                            if (Resultunit == "sq.m") :
                                Result = Result * 10000
                            elif (Resultunit == "sq.km") :
                                Result = Result/10000000000
                        elif (Preferredunit == "sq.m") :
                            if (Resultunit == "sq.cm") :
                                Result = Result/10000
                            elif (Resultunit == "sq.km") :
                                Result = Result * 1000000
                        elif (Preferredunit == "sq.km") :
                            if (Resultunit == "sq.m") :
                                Result = Result/1000000
                            elif (Resultunit == "sq.cm") :
                                Result = Result/10000000000
                        Resultunit = Preferredunit
                    Area = str(Result) + " " + Resultunit
                    print("The Area of the Circle is " + Area + ".")
                except :
                    print("Please Enter Standard Unit of Measurement. (cm/m/km) or (sq.cm/sq.m/sq.km)")
            except :
                print("Please Enter a Numerical Value.")
        else :
            raise ValueError
    except :
        print("Please Enter a Valid Shape.")