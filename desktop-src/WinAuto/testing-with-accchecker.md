---
title: Testing with AccChecker
description: Describes the typical testing workflow that incorporates AccChecker.
ms.assetid: 18C2DDEE-D199-4C22-9ADF-1E07B1325A06
keywords:
- testing with AccChecker
- AccChecker, testing workflow
ms.topic: article
ms.date: 05/31/2018
---

# Testing with AccChecker

The following scenario describes the steps that you typically follow when testing with AccChecker.

> [!Note]  
> When AccChecker verification routines are running, user interaction with the host machine can interfere with some routines. We recommend that no further user interaction occur until AccChecker notifies the user that all tasks are complete.

 

1.  Run AccChecker verifications on a particular target application or control. For more information, see [Verifications Tab](the-accchecker-graphical-user-interface.md).
    > [!Note]  
    > AccChecker doesn't explore all UI permutations in an application. Elements hidden within controls such as windows, panes, tabs, and menus must be exposed manually.

     

2.  Examine the AccChecker error log and assess or triage the results. Fix trivial issues and log severe bugs as appropriate.
3.  Generate a suppression file for bugs and errors that can be ignored until regression testing.
4.  Re-run AccChecker verifications with the suppression file and initial bug fixes. This provides a snapshot of the issues in the current implementation of Microsoft Active Accessibility and establishes a baseline for regression testing.
5.  Integrate the AccChecker APIs and suppression file into an automated test framework for regression testing on bugs logged from the initial AccChecker verifications.
    > [!Note]  
    > As bugs are fixed, the suppression file should be modified as required.

     

6.  Confirm that no regressions or new accessibility bugs have been introduced into the application or control.

## Related topics

<dl> <dt>

[UI Accessibility Checker](ui-accessibility-checker.md)
</dt> </dl>

 

 




