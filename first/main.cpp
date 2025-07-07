#include "common/pch.hpp"
#include "token/token.hpp"
#include "lex/lex.hpp"
#include "test/test.hpp"

using namespace first;

void print(TestResult t)
{
    std::cout << t << std::endl;
}

int main(int argc, char *argv[])
{
    Test t;
    print(t.check_lex("succ 1", "Token(SUCC, 'succ') Token(NUM, '1')"));
    print(t.check_lex("succ ( 1 + x )", "Token(SUCC, 'succ') Token(LPAREN, '(') Token(NUM, '1') Token(UNK, '+') Token(VAR, 'x') Token(RPAREN, ')')"));

    return 0;
}