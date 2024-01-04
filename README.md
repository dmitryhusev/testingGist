`Summary`

Gists provide a simple way to share code snippets with others. Every gist is a Git repository, which means that it can be forked and cloned.

`Scope`

Functional verification testing of the SUT (System under test).

According to test pyramid there are: unit tests, integration tests and end-to-end tests.

Unit tests is dev area of responsibilities, so this is out of scope.

Integration testing is dev/qa area of responsibilities, but since we have only one service this is also out of scope.

E2E testing is qa area of responsibilities, this is the scope of a project.

`Out of scope`

Performance testing

Security testing

`Goals and Deliverables`

Validate the SUT's feature set as specified, claimed, or otherwise made known to us

Provide regression testing

Document the test cases that we create to perform the feature validation: positive cases and negative cases

Produce evidence of our test coverage

`Test Approach`

The "feature set" under test is a service and network API. The requirements/specifications are focused on the JSON request and response bodies.

Test cases and test runs will be recorded in Test management system (N/A, e.g. TestRail).

SUT specification will be recorded in the Issue tracker (N/A, e.g. Jira).

Test coverage will be demonstrated via Allure report.

`Test Harness`

Custom framework (this repo)
