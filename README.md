# Postmortem: The Great Outage of 2024
## Issue Summary

On September 15, 2024, from 2:00 PM to 4:30 PM (UTC), our platform experienced a significant outage affecting the user experience. During this period, the Makalu Market application was entirely unavailable, leading to frustration among users attempting to access our services. Approximately 85% of our active users reported encountering either a blank page or slow loading times. The root cause of the outage was identified as a database connection failure, exacerbated by an unexpected surge in traffic.

## Timeline

2:00 PM (UTC): The issue was detected when automated monitoring alerts indicated a sudden spike in error rates.
2:05 PM (UTC): An engineer on duty noticed the increased error rate and began investigating the service logs.
2:10 PM (UTC): Initial assumptions suggested a possible bug in the new code deployed during the last release.
2:15 PM (UTC): Customer complaints began flooding in via our support channels, highlighting accessibility issues.
2:30 PM (UTC): Investigation revealed high CPU usage on the database server, indicating potential overload.
2:45 PM (UTC): The incident was escalated to the Database Administration team, as the issue appeared related to database connections.
3:00 PM (UTC): Misleading paths included checking application server logs, leading to dead ends in diagnosing the issue.
3:30 PM (UTC): The Database Administration team confirmed that the maximum connection limit was reached due to the influx of traffic, compounded by a misconfigured connection pool.
4:15 PM (UTC): The team resolved the issue by adjusting the database configuration and scaling the connection pool.
4:30 PM (UTC): Services were fully restored, and user access was normalized.

## Root Cause and Resolution

The primary cause of the outage was an overloaded database server that reached its maximum connection limit, preventing new connections from being established. This overload was driven by an unexpected increase in user traffic that coincided with the launch of our latest marketing campaign, which had not been adequately anticipated in our capacity planning.
To fix the issue, we took the following steps:

Increased the maximum number of allowed connections to the database server from 100 to 200.
Reconfigured the connection pooling settings to better manage concurrent connections.
Conducted a thorough analysis of traffic patterns to better prepare for future campaigns.

## Corrective and Preventative Measures

While we successfully resolved the issue, several areas need improvement to prevent future outages:

Improved Capacity Planning: We need to better anticipate traffic surges and adjust our infrastructure accordingly.
Enhanced Monitoring: Implement more granular monitoring on database performance, including real-time alerts for CPU usage and connection limits.

### Action Items:
Patch Database Configuration: Update the database settings to accommodate higher traffic loads.
Implement Connection Pooling: Configure and optimize connection pooling for our database.
Improve Traffic Forecasting: Analyze historical data to improve predictions for traffic spikes.
Set Up Monitoring Alerts: Establish alerts for CPU usage and connection thresholds on the database.
Conduct Load Testing: Perform stress tests before major marketing campaigns to ensure infrastructure can handle increased traffic.

## Conclusion

This incident served as a valuable lesson in capacity planning and the importance of robust monitoring systems. While we managed to restore service, the outage affected a significant portion of our users, reminding us of our commitment to maintaining reliable service. With the corrective actions outlined, we aim to minimize the likelihood of similar issues in the future. And as they say, “If it’s not broke, don’t fix it—but if it is, fix it like a pro!”

![brace yourselves, post mortem is coming meme]("C:\Users\Eunice\Downloads\brace-yourselves-post-b72f1870a8.jpg")
