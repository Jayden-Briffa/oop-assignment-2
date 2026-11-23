| Test id | Pass/fail | Reason | Actions |
| --- | --- | --- | --- |
| 1 | 21 failed, 12 passed | Many tests failed due to invalid title lengths | Correct title validation step in Ticket.py |
| 2 | 2 failed, 29 passed | testValidateTitleInvalidUpper - Failed: DID NOT RAISE ValueError | Wrap title check condition in parentheses |
| 3 | 1 failed, 30 passed | testValidateStatusRejectsChangeBeforeApproval - Failed: DID NOT RAISE ValueError | Implement status validation rule override for FeatureRequest |
| 4 | 31 passed | | |
| 5 (MaCT1) | Fail | Expected ticket creation; got FeatureRequest.__init__() got an unexpected keyword argument 'assignedTechnician' | Update name of technician attribute to assignedTechnician |
| 6 (MaCT1) | Pass | Ticket successfully created | |
| 7 (MaCT2) | Pass | Ticket `2` updated status attribute successfully | |
| 8 (MaCT3) | Pass | Ticket with id `2` was returned and was readable | |
| 9 (MaCT4) | Pass | All tickets were returned with limited detail and were readable | |
| 10 (MaCT5) | Fail | Expected: Only approvable tickets were shown; No tickets appeared | Update filter to look for private _approved attribute |
| 11 (MaCT5) | Pass | Only approvable tickets shown, and weren't shown after approval |
| 12 | 5 failed, 26 passed | All tests failed at a StopIteration | Adjust test input mocking to recognise acknowledgeToContinue and not mock the input if so |
| 13 | 31 passed | | |
