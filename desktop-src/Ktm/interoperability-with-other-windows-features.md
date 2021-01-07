---
description: The Distributed Transaction Coordinator (DTC) enables distributed transactions, or transactions that are under the control of multiple resource managers on one or more systems. KTM and DTC work closely together to accomplish this.
ms.assetid: 468379e2-c5f6-479f-9d5d-42afb395ec9b
title: Interoperability With Other Windows Features
ms.topic: article
ms.date: 05/31/2018
---

# Interoperability With Other Windows Features

The [Distributed Transaction Coordinator](/previous-versions/windows/desktop/ms684146(v=vs.85)) (DTC) enables *distributed transactions*, or transactions that are under the control of multiple resource managers on one or more systems. KTM and DTC work closely together to accomplish this.

COM+ exposes a declarative model for transactional programming. In other words, the programmer declares the extent to which an object can take advantage of transactions, and the COM+ runtime manages the transactions on the object's behalf. For example, an object can be declared to participate in a transaction only if one already exists, to require a transaction (one is created if it does not already exist), to require a new transaction (one is created regardless of whether one already exists), or is not transactional. These declaratively-managed transactions are automatically used on database connections created by COM+ objects that are executing in the context of a transaction.

 

 
