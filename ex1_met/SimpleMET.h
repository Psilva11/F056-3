#ifndef SIMPLEMET_H
#define SIMPLEMET_H

class SimpleMET {
  public:
    SimpleMET();
    SimpleMET(double metx, double mety);


    double Ex() const;
    double Ey() const;
    double Phi() const;
    double Value() const;

    void Add(double px, double py);
  private:
    double metx_;
    double mety_;
    
}; 

#endif