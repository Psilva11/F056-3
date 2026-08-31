SRC			:= testMET.cpp
OUTPUT 	:= testMET

CXX      := g++
LIB      := libSimpleMET.so

all: $(OUTPUT)

SimpleMET.o: SimpleMET.cpp SimpleMET.h
	$(CXX) -fPIC -c SimpleMET.cpp -o SimpleMET.o
$(LIB): SimpleMET.o
	$(CXX) -shared -o $(LIB) SimpleMET.o
$(OUTPUT): testMET.cpp $(LIB)
	$(CXX)  testMET.cpp -L. -lSimpleMET -Wl,-rpath,. -o $(OUTPUT)

clean:
	rm -f *.o $(LIB) $(OUTPUT)
