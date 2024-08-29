1. How the Priority Parameters Were Combined to Determine TRP Priority:
The code determines the TRP priority for each match by assigning a priority score based on various factors such as the series type, rivalry, teams involved, match status, time, match category, format, whether the match is part of a league, gender, and the number of teams in the series.

Steps:

Mapping Priority Values: Each parameter was mapped to a specific priority value based on predefined rules. For instance, World Cup matches received the highest priority under "Series Type," and India-Pakistan matches received the highest priority under "Rivalry."

Assigning Priorities: These priority values were then applied to each match. For example, the teams involved in the match were mapped to a priority score based on their ranking in the priority list.

Combining Priorities: All individual priority scores were summed up to calculate a "Total Priority" score for each match. This score determined the TRP priority, with lower scores indicating higher priority.

Handling Number of Teams: An additional factor was included to give higher priority to series with more teams, where more teams led to a higher priority score.

Sorting Matches: The matches were finally sorted based on their "Total Priority" in ascending order, so those with higher TRP priority (lower scores) appeared first.

2. Assumptions or Simplifications Made:
Equal Weightage: All priority parameters were combined by simple addition, assuming each factor has an equal impact on TRP priority. No additional weighting was applied to emphasize specific parameters.

Time Range Overlaps: For simplicity, time ranges were assumed not to overlap, and each match was assigned a single priority based on its start time. The time priority was determined by the pre-defined ranges without considering the match duration.

Default Values: If a match’s attribute did not match any predefined priority (e.g., if a team wasn't listed), a default priority was assigned, ensuring the match was still ranked.

No Direct Conflicts: It was assumed that no direct conflicts between priorities would arise since they were all handled separately and summed up.

3. How Edge Cases or Conflicting Priorities Were Handled:
Time Priority Assignment: If the match time did not fit neatly into the predefined ranges, the match was assigned the lowest priority (7) by default.

Missing Data: If any data was missing or not matching the priority mappings, the code defaulted to the lowest possible priority for that attribute to avoid errors.

Conflicting Priorities: In cases where multiple factors could potentially conflict (e.g., a match between two low-priority teams but in a high-priority rivalry), the simple sum of priorities naturally resolved conflicts. However, this approach assumes that the combined effect of all factors will accurately reflect the match’s overall priority.

This method effectively ranks matches but could be refined further by applying weights to different factors or by handling specific exceptions more explicitly.







