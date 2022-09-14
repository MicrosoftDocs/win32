---
title: UI guidelines for NDF helper class extensions
description: When building your helper class, you will need to create text to help the user understand the cause of an incident and the possible repair steps which can be taken.
ms.assetid: f13f3621-ab82-4e22-9442-0a4d57c368fc
ms.topic: article
ms.date: 05/31/2018
---

# UI guidelines for NDF helper class extensions

When building your helper class, you will need to create text to help the user understand the cause of an incident and the possible repair steps which can be taken.

## Root Cause and Repair

When an incident occurs, a dialog box will appear to inform the user about what has happened. The text that you create will appear in two separate areas.

-   **Root Cause**: A brief description of the cause of the issue. Contains information to help an administrator or advanced user troubleshoot the problem.
-   **Repair**: Expands on the root cause to provide more details about the steps that a user can take, without getting too lengthy.

Each root cause or repair should have a title and a description. All text before the first "\\n" character will be used for the title. All text following the first "\\n" character (including any subsequent line breaks) will be used for the description.

## Title Guidelines

The title of a root cause or repair should follow these guidelines:

-   Must be 128 characters or fewer. (40 characters or less is recommended.)
-   Should not end with a period.

## Description Guidelines

The description of a root cause or repair should follow these guidelines:

-   Must be 512 characters or fewer.
-   Each sentence should end with a period.
-   The "\\n" character may be used to create a line break in the description.

 

 




