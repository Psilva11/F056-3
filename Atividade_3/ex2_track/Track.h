#ifndef TRACK_H
#define TRACK_H


class Track {
  public:
    Track(double E, double px, double py, double pz);

    double E() const;
    double Px() const;
    double Py() const;
    double Pz() const;

    double Pt() const;
    double Eta() const;

  private:
    double E_;
    double px_;
    double py_;
    double pz_;

};

#endif