---
description: The service control manager (SCM) controls a service by sending service control events to the services control handler routine.
ms.assetid: 86e04b43-5f6f-409e-ac18-d7efada4d3d3
title: Multithreaded Services
ms.topic: article
ms.date: 05/31/2018
---

# Multithreaded Services

The service control manager (SCM) controls a service by sending service control events to the service's control handler routine. The service must respond to control events in a timely manner so that the SCM can keep track of the state of the service. Also, the state of the service must match the description of its state that the SCM receives.

Due to this communication mechanism between a service and the SCM, you must be careful when using multiple threads in a service. When a service is instructed to stop by the SCM, it must wait for all the threads to exit before reporting to the SCM that the service is stopped. Otherwise, the SCM can become confused about the state of the service and might fail to shut down correctly.

The SCM needs to be notified that the service is responding to the stop control event and that progress is being made in stopping the service. The SCM will assume the service is making progress if the service responds (through [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus)) within the time (wait hint) specified in the previous call to **SetServiceStatus**, and the check point is updated to be greater than the checkpoint specified in the previous call to **SetServiceStatus**.

If the service reports to the SCM that the service has stopped before all threads have exited, it is possible that the SCM will interpret this as a contradiction. This might result in a state where the service cannot be stopped or restarted.

 

 



