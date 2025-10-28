package com.alien_breach.demo.controllers;

import com.alien_breach.demo.models.GameState;
import com.alien_breach.demo.models.Player;
import com.alien_breach.demo.services.GameService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/game")
public class GameController {

    @Autowired
    private GameService gameService;

    @PostMapping("/start")
    public ResponseEntity<GameState> start(@RequestBody Player player) {
        return ResponseEntity.ok(gameService.startGame(player));
    }

    @PostMapping("/event/energizer")
    public ResponseEntity<GameState> eventEnergizer(
            @RequestParam Long gameId,
            @RequestParam(defaultValue = "100") int points) {
        GameState updated = gameService.addPoints(gameId, points);
        return ResponseEntity.ok(updated);
    }

    @PostMapping("/event/bonus")
    public ResponseEntity<GameState> eventBonus(
            @RequestParam Long gameId,
            @RequestParam(defaultValue = "400") int points) {
        GameState updated = gameService.addPoints(gameId, points);
        return ResponseEntity.ok(updated);
    }

    @PostMapping("/event/life-lost")
    public ResponseEntity<GameState> eventLifeLost(@RequestParam Long gameId) {
        return ResponseEntity.ok(gameService.loseLife(gameId));
    }

    @PostMapping("/level-up")
    public ResponseEntity<GameState> eventLevelUp(@RequestParam Long gameId) {
        return ResponseEntity.ok(gameService.levelUp(gameId));
    }

    @PostMapping("/state")
    public ResponseEntity<GameState> stateScreen(
            @RequestParam Long gameId,
            @RequestParam String screen) {
        GameState updated = gameService.updateScreen(gameId, screen);
        return ResponseEntity.ok(updated);
    }

    @PostMapping("/over")
    public ResponseEntity<GameState> gameOver(@RequestParam Long gameId) {
        GameState state = gameService.gameOver(gameId);
        return ResponseEntity.ok(state);
    }

}
