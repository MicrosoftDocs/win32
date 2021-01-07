---
description: The following is a list of gesture glyphs that Microsoft plans to support in the future as part of the Microsoft gesture recognizer.
ms.assetid: 4d504140-ff48-4a07-9bf7-a36913e44426
title: Unimplemented Glyphs
ms.topic: article
ms.date: 05/31/2018
---

# Unimplemented Glyphs

The following is a list of gesture glyphs that Microsoft plans to support in the future as part of the *Microsoft gesture recognizer*. Work is in progress to ensure that the recognition accuracy for these glyphs is high (to avoid accidental activation) and that they map to the appropriate operations.

To ensure consistency of *gestures* used for common *actions* between applications, you should adhere to the following suggestions:

-   The *Action* is the suggested semantic behavior associated with the gesture.
-   For the gestures labeled as *Fixed* in the following table, it is recommended that you not change the suggested semantic behavior. If an application does not have a need for the specified semantic behavior, it is recommended that you not reuse the gesture for another action or semantic.
-   You should feel free to associate relevant semantic behaviors to all other gestures. These gestures are labeled as *Application-specific*. For those gestures that have a suggested semantic behavior, it is recommended that you use the gesture for the suggested semantic if the corresponding functionality exists in your application.
-   The hot point of a gesture is a distinguishing point in the geometry of the gesture. The hot point can be used to determine where the gesture was made. The gestures API make it possible to determine the hot point for a given gesture. However, not all gestures have a specific distinguishing hot point. For those that do not have a specific distinguishing hot point, the starting point is reported as the hot point.

> [!Note]  
> Some of the gestures do have a distinguishing hot point that just happens to be the starting point. These are distinguished in the table.

 



| Gesture Name                      | Action                                         | Fixed                           | Hot point                                                           |
|-----------------------------------|------------------------------------------------|---------------------------------|---------------------------------------------------------------------|
| Infinity<br/>               | Switch into and out of gesture mode<br/> | Fixed<br/>                | Starting point<br/>                                           |
| Cross<br/>                  | Delete<br/>                              | Application-specific<br/> | Intersection of the strokes<br/>                              |
| Paragraph mark<br/>         | New paragraph<br/>                       | Fixed<br/>                | Starting point<br/>                                           |
| Section<br/>                | New section<br/>                         | Fixed<br/>                | Starting point<br/>                                           |
| Bullet<br/>                 | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Bullet-cross<br/>           | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Squiggle<br/>               | Bold<br/>                                | Application-specific<br/> | Starting point<br/>                                           |
| Swap<br/>                   | Exchange content<br/>                    | Application-specific<br/> | Middle of the up stroke<br/>                                  |
| Openup<br/>                 | Open up space between words<br/>         | Application-specific<br/> | Middle of the down stroke<br/>                                |
| Closeup<br/>                | Close up extra space<br/>                | Application-specific<br/> | Center of the vertical space between the two parentheses<br/> |
| Rectangle<br/>              | Selects enclosed content<br/>            | Fixed<br/>                | Starting point<br/>                                           |
| Circle-tap<br/>             | Application-specific<br/>                | Application-specific<br/> | Tap<br/>                                                      |
| Circle-circle<br/>          | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Circle-cross<br/>           | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Circle-line-vertical<br/>   | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Circle-line-horizontal<br/> | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Double-arrow-up<br/>        | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Double-arrow-down<br/>      | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Double-arrow-left<br/>      | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Double-arrow-right<br/>     | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Up-arrow-left<br/>          | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Up-arrow-right<br/>         | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Down-arrow-left<br/>        | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Down-arrow-right<br/>       | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Left-arrow-up<br/>          | Application-specific<br/>                | Application-specific<br/> | The apex of the arrow head<br/>                               |
| Left-arrow-down<br/>        | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Right-arrow-up<br/>         | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Right-arrow-down<br/>       | Application-specific<br/>                | Application-specific<br/> | Apex of the arrow head<br/>                                   |
| Diagonal-leftup<br/>        | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Diagonal-rightup<br/>       | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Diagonal-leftdown<br/>      | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Diagonal-rightdown<br/>     | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-A<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-B<br/>         | Bold<br/>                                | Fixed<br/>                | Starting point<br/>                                           |
| Latin-Letter-C<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-D<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-E<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-F<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-G<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-H<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-I<br/>         | Italic<br/>                              | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-J<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-K<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-L<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-M<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-N<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-O<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-P<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-Q<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-R<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-S<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-T<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-U<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-V<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-W<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-X<br/>         | Cut<br/>                                 | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-Y<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Latin-Letter-Z<br/>         | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-0<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-1<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-2<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-3<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-4<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-5<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-6<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-7<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-8<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Digit-9<br/>                | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Question mark<br/>          | Help<br/>                                | Fixed<br/>                | Center along the height of the curve<br/>                     |
| Sharp<br/>                  | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Dollar<br/>                 | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Asterisk<br/>               | Application-specific<br/>                | Application-specific<br/> | Center<br/>                                                   |
| Plus<br/>                   | Paste<br/>                               | Fixed<br/>                | Intersection of the strokes<br/>                              |
| Double-up<br/>              | Scroll up<br/>                           | Fixed<br/>                | Starting point<br/>                                           |
| Double-down<br/>            | Scroll down<br/>                         | Fixed<br/>                | Starting point<br/>                                           |
| Double-left<br/>            | Scroll left<br/>                         | Fixed<br/>                | Starting point<br/>                                           |
| Double-right<br/>           | Scroll right<br/>                        | Fixed<br/>                | Starting point<br/>                                           |
| Triple-up<br/>              | Page up<br/>                             | Fixed<br/>                | Starting point<br/>                                           |
| Triple-down<br/>            | Page down<br/>                           | Fixed<br/>                | Starting point<br/>                                           |
| Triple-left<br/>            | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Triple-right<br/>           | Application-specific<br/>                | Application-specific<br/> | Starting point<br/>                                           |
| Bracket-over<br/>           | Application-specific<br/>                | Application-specific<br/> | Midpoint<br/>                                                 |
| Bracket-under<br/>          | Application-specific<br/>                | Application-specific<br/> | Midpoint<br/>                                                 |
| Bracket-left<br/>           | Start of selection<br/>                  | Fixed<br/>                | Midpoint<br/>                                                 |
| Bracket-right<br/>          | End of selection<br/>                    | Fixed<br/>                | Midpoint<br/>                                                 |
| Brace-over<br/>             | Application-specific<br/>                | Application-specific<br/> | Midpoint<br/>                                                 |
| Brace-under<br/>            | Application-specific<br/>                | Application-specific<br/> | Midpoint<br/>                                                 |
| Brace-left<br/>             | Start of discontinuous selection<br/>    | Fixed<br/>                | Midpoint<br/>                                                 |
| Brace-right<br/>            | End of discontinuous selection<br/>      | Fixed<br/>                | Midpoint<br/>                                                 |
| Triple-tap<br/>             | Application-specific<br/>                | Application-specific<br/> | Starting point is distinguishing hot point<br/>               |
| Quadruple-tap<br/>          | Application-specific<br/>                | Application-specific<br/> | Starting point is distinguishing hot point<br/>               |



 

 

 




