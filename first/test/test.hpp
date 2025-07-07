#pragma once
#include "../common/pch.hpp"
#include "../lex/lex.hpp"
#include "../token/token.hpp"

namespace first
{
    class TestResult
    {
    public:
        bool success;
        std::string message;
        TestResult(bool success, const std::string &message) : success(success), message(message) {}
        friend std::ostream &operator<<(std::ostream &os, const TestResult &test_result);
    };

    class Test
    {
        Lexer lexer;

    public:
        Test() : lexer("") {}
        ~Test() = default;
        TestResult check_lex(const std::string &input, const std::string &expected);
    };

    std::ostream &operator<<(std::ostream &os, const TestResult &result);
}