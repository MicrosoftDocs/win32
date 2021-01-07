---
description: You use the PDH functions to collect performance data.
ms.assetid: 2510480e-cfea-4f7c-af0b-6d229c150c91
title: Using the PDH Functions to Consume Counter Data
ms.topic: article
ms.date: 08/17/2020
---

# Using the PDH Functions to Consume Counter Data

Use the PDH functions to collect performance data. The PDH functions are easier to use than the [registry functions](using-the-registry-functions-to-consume-counter-data.md) and can be used to access counter data both V1 and V2 providers. PDH has APIs for collecting current performance data, saving performance data to log files, and reading data from log files.

> [!Note]
> You cannot use the Performance Data Helper abstraction-layer functions if you are writing Windows OneCore apps. Instead, use [PerfLib V2 Consumer functions](using-the-perflib-functions-to-consume-counter-data.md).

PDH is a high-level API that simplifies collecting performance counter data. It helps with query parsing, metadata caching, matching up instances between samples, computing formatted values from raw values, reading data from log files, and saving data to log files. PDH automatically uses the [registry functions](using-the-registry-functions-to-consume-counter-data.md) when collecting data from **V1 providers** and it uses the [V2 Consumer functions](using-the-perflib-functions-to-consume-counter-data.md) when collecting data from **V2 providers**.

To collect performance data using the PDH functions, perform the following steps.

1. [Create a query](creating-a-query.md)
2. [Add counters to the query](creating-a-query.md)
3. [Collect the performance data](collecting-performance-data.md)
4. [Display the performance data](displaying-performance-data.md)
5. [Close the query](creating-a-query.md)

You can collect performance data from either real-time sources or log files. For more information on how to write performance data to log files, see [Working with Log Files](working-with-log-files.md).

## See also

- [Collecting Performance Data](collecting-performance-data.md)
- [Browsing Counters](browsing-counters.md)
- [Checking PDH Interface Return Values](checking-pdh-interface-return-values.md)
- [Examples](examples.md)
