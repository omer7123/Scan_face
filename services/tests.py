from fastapi import Query

# from shemas.tests import CreateTest, Test, TestInfo, PlayTest
# import sql.db.db_tests as db
# import sql.db.db as db_user
# from shemas.users import UserInfo
#
#
# class TestService:
#
#     def add_test(self, test: CreateTest) -> CreateTest:
#         if db_user.token_verification(test.user.token, test.id_authors):
#             return db.create_test(test)
#
#     def get_tests(self, id_user: str = Query(...), token: str = Query(...)) -> list[TestInfo]:
#         if db_user.token_verification(token, id_user):
#             return db.get_tests(id_user)
#
#
#
# test_service: TestService = TestService()
