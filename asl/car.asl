/**
 * @author	Patrick Gavigan
 * @date	17 March 2020
 */

// Initial goal 
!drive.
 
// Main plan
+!drive
	:	lkaSteering(ANGLE) |
		throttle(THROTTLE) |
		brake(BRAKE)
	<-	setThrottle(1.0);
		!drive.
		
// Catch plan
+!drive
	<-	!drive.

