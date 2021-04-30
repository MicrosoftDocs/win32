---
description: The return value of PDH functions indicates the success or failure of the function call, which is different from the status of the counter data.
ms.assetid: 00ea5521-bc28-4a87-aba9-46c911631503
title: Checking Counter Data Status Codes
ms.topic: article
ms.date: 05/31/2018
---

# Checking Counter Data Status Codes

The return value of PDH functions indicates the success or failure of the function call, which is different from the status of the counter data. Always check the **CStatus** member of a counter value returned in the PDH structures to ensure that the data returned is valid before you use it. If the value of the **CStatus** member does not indicate success, do not use the data. The following are the possible status values for counters:



| Value                              | Meaning                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PDH\_CSTATUS\_NO\_MACHINE          | PDH was unable to connect to the computer specified in the counter path. If this status is returned when the counter is being added, the counter is not completely initialized. Each time the query is updated, PDH retries the connection. When the connection is established, normal data collection resumes.                                                                  |
| PDH\_CSTATUS\_NO\_OBJECT           | The specified computer was found, but the specified performance object was found on the computer. If this status is returned when the counter is being added, the specified counter is not included in the query. If this status is returned by an active counter, the data for that counter is invalid. Each time the data is requested, PDH tries to obtain this counter data. |
| PDH\_CSTATUS\_NO\_INSTANCE         | The specified instance was not found in the object. If this status is returned while the counter is being added to the query, the counter is successfully added to the query, but no data is available until the specific instance appears and a successful status is returned.                                                                                                  |
| PDH\_CSTATUS\_NO\_COUNTER          | The specified counter was not found in the specified object. If this status is returned when the counter is being added, then the counter is not added to the query. If this status is returned after data collection, the data for that counter is invalid. Each time the data is requested, PDH tries to obtain this counter data.                                             |
| PDH\_CSTATUS\_INVALID\_DATA        | The counter was successfully found, but the data returned is not valid. This error can occur if the counter value is less than the previous value. (Because counter values always increment, the counter value rolls over to zero when it reaches its maximum value.) Another possible cause is a system timer that is not correct.                                              |
| PDH\_CSTATUS\_VALID\_DATA          | The data for the counter was returned successfully, but is unchanged from the last time the counter was read.                                                                                                                                                                                                                                                                    |
| PDH\_CSTATUS\_NEW\_DATA            | The data for the counter was returned successfully and is different from the last time the counter was read. PDH\_CSTATUS\_NEW\_DATA can be returned on a rate counter even if the resulting rate is the same as the last sample. This is because the raw data value that is used in the determination of this status value has changed, not the computed rate.                  |
| PDH\_MORE\_DATA                    | The supplied buffer was not large enough to store all of the counter data. Allocate a larger buffer and execute the function again.                                                                                                                                                                                                                                              |
| PDH\_CSTATUS\_ITEM\_NOT\_VALIDATED | The counter has been added to the query, but has not been validated nor accessed. No additional status information on this counter is available.                                                                                                                                                                                                                                 |
| PDH\_CSTATUS\_NO\_COUNTERNAME      | No counter name was specified in the query.                                                                                                                                                                                                                                                                                                                                      |
| PDH\_CSTATUS\_NO\_COUNTER          | The specified counter name could not be found.                                                                                                                                                                                                                                                                                                                                   |
| PDH\_CSTATUS\_NO\_OBJECT           | The specified performance object could not be found.                                                                                                                                                                                                                                                                                                                             |
| PDH\_CALC\_NEGATIVE\_DENOMINATOR   | A counter has a negative denominator value.                                                                                                                                                                                                                                                                                                                                      |
| PDH\_CALC\_NEGATIVE\_TIMEBASE      | A counter has a negative timebase value.                                                                                                                                                                                                                                                                                                                                         |
| PDH\_CALC\_NEGATIVE\_VALUE         | A counter has a negative value.                                                                                                                                                                                                                                                                                                                                                  |
| PDH\_CSTATUS\_NO\_COUNTERNAME      | No counter path was specified.                                                                                                                                                                                                                                                                                                                                                   |
| PDH\_CSTATUS\_BAD\_COUNTERNAME     | The counter path format is incorrect.                                                                                                                                                                                                                                                                                                                                            |



 

 

 



