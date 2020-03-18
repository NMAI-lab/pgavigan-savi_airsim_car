/**
 * @author	Patrick Gavigan
 * @date	17 March 2020
 */

// Rules
//NoBreak :-
//	((brake(B) & B == 0) |
//	(not brake(B)))
 
// Initial goal 
!drive.
 
// Main plan
+!drive
	:	lkaSteering(STEERING) &
		throttle(THROTTLE) &
		brake(BRAKE)
	<-	setBrake(BRAKE);
		setSteering(STEERING);
		setThrottle(THROTTLE);
		!drive.
		
+!drive
	:	lkaSteering(STEERING) &
		throttle(THROTTLE) &
		not brake(BRAKE)
	<-	setSteering(STEERING);
		setThrottle(THROTTLE);
		setBrake(0);
		!drive.
		
+!drive
	:	lkaSteering(STEERING) &
		not throttle(THROTTLE) &
		brake(BRAKE)
	<-	setSteering(STEERING);
		setThrottle(0);
		setBrake(BRAKE);
		!drive.
		
+!drive
	:	not lkaSteering(STEERING) &
		throttle(THROTTLE) &
		brake(BRAKE)
	<-	setThrottle(THROTTLE);
		setBrake(BRAKE);
		!drive.
		
+!drive
	:	lkaSteering(STEERING) &
		not throttle(THROTTLE) &
		not brake(BRAKE)
	<-	setSteering(STEERING);
		!drive.
		
+!drive
	:	not lkaSteering(STEERING) &
		throttle(THROTTLE) &
		not brake(BRAKE)
	<-	setThrottle(THROTTLE);
		!drive.
		
+!drive
	:	not lkaSteering(STEERING) &
		not throttle(THROTTLE) &
		brake(BRAKE)
	<-	setBrake(BRAKE);
		!drive.
		
// Catch plan
+!drive
	<-	!drive.

