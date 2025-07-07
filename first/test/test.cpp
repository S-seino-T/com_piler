#include "test.hpp"

namespace first
{

    TestResult Test::check_lex(const std::string &input, const std::string &expected)
    {
        first::Lexer lexer(input);
        std::vector<first::Token> tokens = lexer.tokenize();
        std::string result;
        for (const auto &token : tokens)
        {
            if (!result.empty())
                result += " ";
            result += token.to_string();
        }
        if (result == expected)
        {
            return TestResult(true, "OK");
        }
        else
        {
            return TestResult(false, "Expected:\t" + expected + "\tBut got:\t" + result);
        }
    }

    std::ostream &operator<<(std::ostream &os, const TestResult &result)
    {
        os << (result.success ? "Success: " : "Failure: ") << result.message;
        return os;
    }

}