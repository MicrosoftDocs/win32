---
description: The CounterData table contains a row for each counter that is collected at a particular time. There will be a large number of these rows.
ms.assetid: 1253a9c7-b440-4ff2-b68c-c52b9b42a58b
title: CounterData
ms.topic: article
ms.date: 05/31/2018
---

# CounterData

The **CounterData** table contains a row for each counter that is collected at a particular time. There will be a large number of these rows.

The **CounterData** table defines the following fields:

-   **GUID:** GUID for this data set. Use this key to join with the [**DisplayToID**](displaytoid.md) table.
-   **CounterID:** Identifies the counter. Use this key to join with the [**CounterDetails**](counterdetails.md) table.
-   **RecordIndex:** The sample index for a specific counter identifier and collection GUID. The value increases for each successive sample in this log file.
-   **CounterDateTime:** The time the collection was started, in UTC time.
-   **CounterValue:** The formatted value of the counter. This value may be zero for the first record if the counter requires two sample to compute a displayable value.
-   **FirstValueA:** Combine this 32-bit value with the value of **FirstValueB** to create the **FirstValue** member of [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter). **FirstValueA** contains the low order bits.
-   **FirstValueB:** Combine this 32-bit value with the value of **FirstValueA** to create the **FirstValue** member of [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter). **FirstValueB** contains the high order bits.
-   **SecondValueA:** Combine this 32-bit value with the value of **SecondValueB** to create the **SecondValue** member of [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter). **SecondValueA** contains the low order bits.
-   **SecondValueB:** Combine this 32-bit value with the value of **SecondValueA** to create the **SecondValue** member of [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter). **SecondValueB** contains the high order bits.

The **GUID**, **CounterID**, and **RecordIndex** fields make up the primary key for this table.

 

 



