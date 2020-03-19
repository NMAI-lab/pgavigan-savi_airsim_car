/**
 * @author	Patrick Gavigan
 * @date	18 March 2020
 */

// Initial goal: drive the car
!drive.

// I have brake, throttle and steering
+!drive
	:	speedControl(BRAKE,THROTTLE) & steering(STEERING)
	<-	driveActionBTS(BRAKE,THROTTLE,STEERING)
		!drive.
		
// I have brake and throttle, not steering
+!drive
	:	speedControl(BRAKE,THROTTLE) & (not steering(_))
	<-	driveActionBT(BRAKE,THROTTLE)
		!drive.
		
// I have steering, note brake and not throttle
+!drive
	:	(not speedControl(_,_)) & steering(STEERING)
	<-	driveActionBT(BRAKE,THROTTLE)
		!drive.

// I have steering, not brake or throttle 
+!drive
	:	((not brake(_)) & (not throttle(_))) & steering(STEERING)
	<-	setSteering(STEERING);
		!drive.		
		
/*		
// Drive car - set the brake
+!drive
	:	brake(BRAKE) & not throttle(_)
	<-	setBrake(BRAKE);
		setThrottle(0);
		!steer;
		!drive.

// Drive the car - set the throttle
+!drive
	: 	throttle(THROTTLE) & not brake(_)
	<-	setBrake(0);
		setThrottle(THROTTLE);
		!steer;
		!drive.

// Plan to ensure recursion
+!drive
	<-	!drive.
		
// Steer the car
+!steer
	:	lkaSteering(STEERING)
	<-	setSteering(STEERING).
	
// Default plan for steering
+!steer.
*/
