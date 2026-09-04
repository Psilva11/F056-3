#include "SimpleMET.h"
#include <cmath>

SimpleMET::SimpleMET() : metx_(0.0), mety_(0.0) {}
SimpleMET::SimpleMET(double metx, double mety) : metx_(metx), mety_(mety) {}


double SimpleMET::Ex() const {
  return metx_;
}
double SimpleMET::Ey() const {
  return mety_;
}
double SimpleMET::Phi() const {
  return std::atan2(mety_, metx_);
}
double SimpleMET::Value() const {
  return std::sqrt(metx_ * metx_ + mety_ * mety_);
}

void SimpleMET::Add(double px, double py) {
    metx_ -= px;
    mety_ -= py;
}