PYTHIA_DIR = /home/pedro/Downloads/pythia8315

CXX = g++
CXXFLAGS = -O2 -Wall -std=c++17 $(shell root-config --cflags) -I$(PYTHIA_DIR)/include
LDFLAGS = $(shell root-config --libs) -L$(PYTHIA_DIR)/lib -lpythia8

SOURCES = $(wildcard *.cc)
TARGETS = $(SOURCES:.cc=)

all: $(TARGETS)

%: %.cc
	$(CXX) $(CXXFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f main *.root *.png *.o