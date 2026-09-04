#include "Track.h"
#include <cmath>
#include <iostream>

Track::Track(double E, double px, double py, double pz) : E_(E), px_(px), py_(py), pz_(pz) {}


double Track::E() const {
  return E_;
}
double Track::Px() const {
  return px_;
}
double Track::Py() const {
  return py_;
}
double Track::Pz() const {
  return pz_;
}

double Track::Pt() const {
  return std::sqrt(px_ * px_ + py_ * py_);
}
double Track::Eta() const {
  double pt = Pt();

  // Trata o caso pt == 0 com um limite de tolerancia
  if (pt < 1e-9) {
    if (pz_ > 0) return std::numeric_limits<double>::infinity();
    if (pz_ < 0) return -std::numeric_limits<double>::infinity();
    return 0.0; // Particula totalmente parada (p = 0)
  }

  double p = std::sqrt(px_ * px_ + py_ * py_ + pz_ * pz_);
  double theta = std::acos(pz_ / p);
  return -std::log(std::tan(theta / 2.0));
}