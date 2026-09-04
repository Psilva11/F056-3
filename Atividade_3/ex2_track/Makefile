SRC			:= testTrack.cpp
OUTPUT 	:= testTrack

CXX      := g++
LIB1      := libTrack.so
LIB2			:= libSimTrack.so

all: $(OUTPUT)

Track.o: Track.cpp Track.h
	$(CXX) -fPIC -c Track.cpp -o Track.o
$(LIB1): Track.o
	$(CXX) -shared -o $(LIB1) Track.o

SimTrack.o: SimTrack.cpp SimTrack.h
	$(CXX) -fPIC -c SimTrack.cpp -o SimTrack.o
$(LIB2): SimTrack.o $(LIB1)
	$(CXX) -shared -o $(LIB2) SimTrack.o -L. -lTrack -Wl,-rpath,.

$(OUTPUT): testTrack.cpp $(LIB1) $(LIB2)
	$(CXX)  testTrack.cpp -L. -lTrack -lSimTrack -Wl,-rpath,. -o $(OUTPUT)

clean:
	rm -f *.o *.so $(OUTPUT)
