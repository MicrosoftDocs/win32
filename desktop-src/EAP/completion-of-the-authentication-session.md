---
title: Completion of the Authentication Session
description: After the authentication session is completed, the authentication service calls the RasEapEnd function to allow the authentication protocol to deallocate its work buffer.
ms.assetid: 466795ac-fee5-4b82-adc7-af14b6ef3fc3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Completion of the Authentication Session

After the authentication session is completed, the authentication service calls the [**RasEapEnd**](https://www.bing.com/search?q=**RasEapEnd**) function to allow the authentication protocol to deallocate its work buffer. This action is taken regardless of whether authentication was successful. Calling the **RasEapEnd** function guarantees that no further calls are made to the authentication protocol using that particular user or context without first calling [**RasEapBegin**](https://www.bing.com/search?q=**RasEapBegin**).

 

 




