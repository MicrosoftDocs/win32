---
title: Testing a User Interface
description: This section describes in detail some of the tasks associated with testing a UI for a Windows application.
ms.assetid: d628e530-7a0b-4a8d-9a9f-253aec275fa9
ms.topic: article
ms.date: 05/31/2018
---

# Testing a User Interface

This section describes in detail some of the tasks associated with testing a UI for a Windows application.

-   [Introduction](#introduction)
-   [Usability Testing](#usability-testing)
-   [Accessibility Testing](#accessibility-testing)

## Introduction

To fully determine the effectiveness and overall usability of an application UI, it must be tested. Testing exposes how easy or difficult the UI is to use for the broadest possible audience. The time that it takes to test an application is well worth it.

This topic focuses on three primary testing scenarios: general usability, accessibility, and automation.

## Usability Testing

Usability testing provides the opportunity to evaluate a product by studying how real users actually use the product. This analysis ensures that key assumptions about intended users and interface designs are supported (or challenged) with real data. Only by gathering this empirical data can you find out how well the UI for a product fits your users' needs and expectations.

By observing user interaction with the product and listening to user feedback, important features that may be difficult to find and use are identified. Based on these results, adjustments can be made to the UI as required. It is almost impossible to build a useful product without some level of usability testing as the results provide the basis for making better decisions about the product and improving the overall user experience.

Usability testing provides significant payback only when it is well integrated into the entire project lifecycle. A single usability study can identify issues, but without follow-up tests it is difficult to determine if the solutions have solved those problems or introduced new ones.

The primary scenarios for usability testing are:

-   If you are a software product vendor, testing real users of your product means you are evaluating the design. Based on how you have designed the application, can users complete the tasks they need to do? Testing real users doing real tasks can also point out if the UI guidelines you are following are working within the context of your product, and when consistency helps or hinders the ability of a user to do their work.
-   If you are a software product purchaser, you can do usability testing to evaluate a product for purchase. For example, your company might consider buying a product for their twenty thousand employees. Before the company spends its money, it wants to make sure that the product in question will really help employees do their jobs better. Usability testing can also be useful to see if the proposed application follows published UI style guidelines (internal or external). It's best to use UI guidelines as an auxiliary, rather than primary, source of information for making purchase decisions.

For more information, see [Usability in Practice: Usability Testing](/archive/msdn-magazine/2009/brownfield/usability-in-practice-usability-testing).

## Accessibility Testing

Accessibility testing encompasses two areas of a UI design: support for users with disabilities and programmatic access by automated test frameworks.

Ensuring that an application is accessible to users with disabilities involves testing for:

-   Compliance - Does the application comply with various legal requirements regarding accessibility?
-   Effectiveness - Can users with disabilities use the application?
-   Usefulness - Does the application expose adequate functionality for users with disabilities?
-   Satisfaction - How is the application perceived by users with disabilities?

Testing for these aspects of an application can be accomplished through an accessibility audit, which involves a manual review of the application by an accessibility expert, and a focused usability study of disabled users and assistive technology devices.

Although seemingly unrelated, there is a close correlation between the programmatic access requirements of automated test frameworks and those of assistive technology devices. Supporting one has the added benefit of enabling the other. For more information on accessibility and test automation in Windows applications, see [Accessibility](/windows/desktop/accessibility), [Testing Tools](/windows/desktop/WinAuto/testing-tools), and the [Windows Automation API](/windows/desktop/WinAuto/windows-automation-api-portal).

 

 