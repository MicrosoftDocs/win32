---
description: Synchronization values can be automatically determined or constrained by the configuration of other properties, such as transactional requirements and just-in-time (JIT) activation.
ms.assetid: 16771121-cb10-42b4-babc-59270188495a
title: Synchronization Dependencies
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Dependencies

Synchronization values can be automatically determined or constrained by the configuration of other properties, such as transactional requirements and just-in-time (JIT) activation. For example, COM+ enforces synchronization both for transactional and for JIT-activated components.

These dependencies exist because components that are JIT-activated or participating in transactions must have proper isolation and concurrency behavior. Therefore, COM+ requires that access to these components be serialized by enforcing synchronization. (For details on these dependencies, see [COM+ Just-in-Time Activation](com--just-in-time-activation.md).)

The following tables show the characteristics of the COM+ synchronization attribute values.

### Transactional requirement



| When transactions are set to | Synchronization can be set to                    |
|------------------------------|--------------------------------------------------|
| Disabled<br/>          | Anything, depending on JIT activation<br/> |
| Not Supported<br/>     | Anything, depending on JIT activation<br/> |
| Supported<br/>         | Required<br/>                              |
| Required<br/>          | Required<br/>                              |
| Requires New<br/>      | Required or Requires New<br/>              |



 

### JIT Activation



| When JIT Activation is set to | Synchronization can be set to       |
|-------------------------------|-------------------------------------|
| Enabled<br/>            | Required or Requires New<br/> |
| Disabled<br/>           | Anything<br/>                 |



 

For more detail about how transaction, JIT Activation, and Synchronization attributes behave together, see [Configuring Transactions](configuring-transactions.md).

## Related topics

<dl> <dt>

[Setting the Synchronization Attribute](setting-the-synchronization-attribute.md)
</dt> <dt>

[Synchronization Attribute Values](synchronization-attribute-values.md)
</dt> </dl>

 

 




