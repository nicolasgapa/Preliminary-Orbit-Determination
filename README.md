# Preliminary-Orbit-Determination

Author: Nicolas Gachancipa

Obtain orbit position and velocity vectors from ground-based angle and range measurements.

This algorithm obtains position and velocity (R and V) vectors in the Earth-centered inertial (ECI) coordinate frame, given ground-based angle and range measurements for an orbital element (e.g. satellite) in the Topocentric horizon (SEZ) frame.

The topocentric frame has its origin at a ground-station (e.g. a point on the surface of the earth) and its fixed with respect to earth’s surface (i.e. does not change as the earth rotates). The ECI frame has its origin at the center of the earth.

The code takes six values as inputs: 
        
        ρ:range-distance from ground station to satellite (in km.)
        
        σ:elevation angle (in degrees)
        
        β:azymuth angle (in degrees)
        
        dρ: rate of change of range (in km per second)

        dσ: rate of change of elevation angle (in degrees per second)

        dβ: rate of change of azymuth angle (in degrees per second)

The coordinates (latitude and longitude) of the ground-based station must also be defined.

        φ:latitude

        λ:longitude
        
The algorithm returns the position (R) and velocity (V) vectors of the satellite at the given instance.
