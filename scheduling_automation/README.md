# Scheduling Automation

Meditrina must suggest to the Nurse which days to invite the Patient back in. Each patient has a dosing prescription that gives a recommended schedule for taking medication. Of course some days the office is not open.

Meditrina is going to provide the nurse instant reschedule suggestions at the conclusion of a dosing event.

# Prescription Dosing Days by Schedule Phase

### Given:

- a prescription object with defined schedule intervals
- a blackout date and time list
- a most current dose
- maximum 1 dose per day

### Provide:

a function that will return the next N suggested dates that spaces the schedule out evenly across a calendar.

### Requirements:

- Returns a list of N datetime objects
- Must respect blackout dates (holidays, business closures)
- Will have a static blackout day of Sunday
- Takes a prescription object, blackout date/time list
- Will use last dosing event for time suggestion.


## Prescription Phase Example

Every business may change the numbers in their settings. For instance they may have Phase II as dosing 2x per week or Phase VI as dosing monthly. The user may define Phase I as 7x weekly or 1x daily.

- Phase I
	– Dose 1x daily
- Phase II
	– Dose 3x weekly
	- Schedule Examples
		- M, W, F
		- T, TH, S
- Phase III
	– Dose 2x weekly
	- Schedule Examples
		- M, TH
		- M, F
		- T, F
		- T, S
		- W, S
- Phase IV
	- Dose 1x weekly
- Phase V
	- Dose 2x monthly
	- Biweekly


### PrescriptionSchedule object

```
                        Table "public.dosing_prescription_schedule"
   Column    |           Type           | Modifiers | Storage  | Stats target | Description
-------------+--------------------------+-----------+----------+--------------+-------------
 id          | uuid                     | not null  | plain    |              |
 business_id | uuid                     | not null  | plain    |              |
 created     | timestamp with time zone | not null  | plain    |              |
 name        | character varying(25)    | not null  | extended |              |
 monthly     | integer                  |           | plain    |              |
 weekly      | integer                  |           | plain    |              |
 daily       | integer                  |           | plain    |              |
```

### Suggestions

- Use primitives and math
- Don't use giant if/else or case statements
- See unix cron logic

### Bonus round if python

- Unit test cases
- Validity checking on parameters and data fields

### INFO

Estimated code time: < 1 hour

Bounty: $50

Start Date: 2016-08-04
