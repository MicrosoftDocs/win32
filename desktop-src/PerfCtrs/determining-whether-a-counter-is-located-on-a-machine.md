---
description: To determine if a counter is installed on a particular computer, call PdhValidatePath with the fully qualified counter path. The function returns ERROR\_SUCCESS if the counter is located on the specified computer.
ms.assetid: 5533a8d8-3621-4ce7-984c-c3895adef531
title: Determining Whether a Counter Is Located on a Computer
ms.topic: article
ms.date: 05/31/2018
---

# Determining Whether a Counter Is Located on a Computer

To determine if a counter is installed on a particular computer, call [**PdhValidatePath**](/windows/desktop/api/Pdh/nf-pdh-pdhvalidatepatha) with the fully qualified counter path. The function returns ERROR\_SUCCESS if the counter is located on the specified computer.

[**PdhValidatePath**](/windows/desktop/api/Pdh/nf-pdh-pdhvalidatepatha) validates the entire path; therefore, if any object, instance, or counter in the path does not exist, the return value indicates so. **PdhValidatePath** verifies the specified counter path in this order: computer, performance object, instance, and counter.

 

 



